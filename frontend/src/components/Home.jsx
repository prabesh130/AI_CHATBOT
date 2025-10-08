import { Link} from "react-router-dom";
import imagePlaceholder from "../images/chat.jpg"
import Features from "./Features";

export default function Home() {
    return (
        <>
            <div className="w-full h-[calc(100vh-70px)] bg-[#d6f5d6] grid place-content-center">
                <div className="w-[1280px] h-[500px] bg-[#eafaea] flex">
                    <div className="w-1/2 h-full flex flex-col items-center justify-center gap-7 px-14">
                        <div className="text-7xl font-semibold">Intelligent conversation at your fingertips</div>
                        <div className="text-xl">Unlock the power of advanced AI communication. Our chatbot understands context, learns from interactions, and delivers precise responses.</div>
                        <div className="w-full flex gap-5 text-lg font-semibold">
                            <div className="w-[120px] h-[45px] bg-[#1e90ff] grid place-content-center rounded-md shadow-[0_5px_0_#1873cc] duration-75 active:translate-y-[3px] active:shadow-[1px_2px_0_#1873cc]">
                                <Link className="text-white" to="/signup">Try now</Link>
                            </div>
                            <div className="w-[140px] h-[45px] bg-[#c0ffbb] grid place-content-center rounded-md shadow-[0_5px_0_#B6B4B3] duration-75 active:translate-y-[3px] active:shadow-[1px_2px_0_#B6B4B3]">
                                <a className="" href="#features">Learn more</a>
                            </div>
                        </div>
                    </div>
                    <div className="w-auto h-full">
                        <img className="w-full h-full" src={imagePlaceholder} alt="chatbot" />
                    </div>
                </div>
            </div>

            <div id="features">
                <Features />
            </div>
        </>
    )
}